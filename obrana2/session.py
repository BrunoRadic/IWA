import db, os, articles
from http import cookies

def get_or_create_session_id():

    cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

    if "session_id" in cookie:
        session_id = cookie["session_id"].value
        existing_id, _ = db.get_session(session_id)
        if existing_id is not None:
            return session_id, None
        
    session_id = db.create_session()
    new_cookie = cookies.SimpleCookie()
    new_cookie["session_id"] = session_id
    return session_id, new_cookie

def get_session_data(session_id):
    _, data = db.get_session(session_id)
    return data

def saveArticles(session_id, params):
    data = get_session_data(session_id)
    for key in articles.articles:
        if params.getvalue(str(key)) == "yes":
            data[str(key)] = params.getvalue(str(key))
        else:
            data.pop(str(key), None)
    db.update_session(session_id, data)