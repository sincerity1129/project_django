class SessionController:
    def user_session_in(request, user_email, session_name='email'):
        request.session[session_name] = user_email
    
    def user_session_out(request, session_name='email', other_user_session='id'):
        request.session[session_name] = None
        request.session[other_user_session] = None  
        
    def other_user_seesion_in(request, user_id, session_name='id'):
        request.session[session_name] = user_id
    
    
def json_merge(**separate_column):
    return dict(separate_column)