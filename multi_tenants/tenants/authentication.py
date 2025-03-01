from rest_framework_simplejwt.authentication import JWTAuthentication

class TenantJWTAuthentication(JWTAuthentication):
    def authentication(self,request):
        auth_result=super().authenticate(request)
        if auth_result is None:
            return None
        user,token=auth_result
        request.tenant=user.tenant
        return  user,token