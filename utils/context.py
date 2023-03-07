from contextvars import ContextVar

REQUEST_ID_CTX_KEY = "request_id"
request_id_ctx_var: ContextVar[str] = ContextVar(REQUEST_ID_CTX_KEY, default=None)


def get_request_id():
    return request_id_ctx_var.get()
