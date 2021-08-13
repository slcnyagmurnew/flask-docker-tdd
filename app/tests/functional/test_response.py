import json
from app import app


def test_find_page():
    flask_app = app.app
    flask_app.config['TESTING'] = True
    flask_app.config['DEBUG'] = False
    flask_app.config['WTF_CSRF_ENABLED'] = False
    with flask_app.test_client() as test_client:
        response = test_client.get('/find/Lancelot')
        result = json.loads(response.data.decode("utf-8"))
        assert response.status_code == 200
        assert result["favorite_color"][0]["Lancelot"] == "blue"
