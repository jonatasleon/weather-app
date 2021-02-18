from functools import wraps

from flask import Blueprint

from api.core.models import HistoryModel

from .extensions import db, owm

api = Blueprint("api", __name__)


def save_history(f):
    @wraps(f)
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)

        to_save = result
        if isinstance(result, tuple):
            to_save = result[0]

        history = HistoryModel(result=to_save)
        db.session.add(history)
        db.session.commit()

        return result

    return inner


@api.route("/forecast/<city>")
@save_history
def forecast(city):
    result = owm.forecast(city)
    if result.status_code != 200:
        return result.json(), result.status_code
    return result.json()


@api.route("/history")
def get_history():
    entities = (
        HistoryModel.id,
        HistoryModel.result["city"]["name"],
        HistoryModel.queried_at,
    )
    query = db.session.query(*entities)
    history = [dict(zip(["id", "city_name", "queried_at"], u)) for u in query.all()]
    return {"history": history}


@api.route("/history/<id>")
def get_history_by_id(id):
    entities = (
        HistoryModel.id,
        HistoryModel.result,
        HistoryModel.queried_at,
    )
    query = (
        db.session.query(HistoryModel)
        .filter(HistoryModel.id == id)
        .with_entities(*entities)
    )
    result = query.first_or_404(
        description=f"Not found a history registry with id {id}"
    )
    return dict(zip(["id", "result", "queried_at"], result))
