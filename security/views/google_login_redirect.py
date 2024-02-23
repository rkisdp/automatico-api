# # Step 1

# from attrs import define
# from django.conf import settings


# @define
# class GoogleRawLoginCredentials:
#     client_id: str
#     client_secret: str
#     project_id: str


# def google_sdk_login_get_credentials() -> GoogleRawLoginCredentials:
#     client_id = settings.OAUTH2_GOOGLE_CLIENT_ID
#     client_secret = settings.OAUTH2_GOOGLE_CLIENT_SECRET
#     project_id = settings.OAUTH2_GOOGLE_PROJECT_ID

#     credentials = GoogleRawLoginCredentials(
#         client_id=client_id,
#         client_secret=client_secret,
#         project_id=project_id,
#     )

#     return credentials


# from django.conf import settings
# from django.urls import reverse_lazy


# class GoogleSdkLoginFlowService:
#     API_URI = reverse_lazy("api:google-oauth2:login-sdk:callback-sdk")

#     # Two options are available: 'web', 'installed'
#     GOOGLE_CLIENT_TYPE = "web"

#     GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
#     GOOGLE_ACCESS_TOKEN_OBTAIN_URL = "https://oauth2.googleapis.com/token"
#     GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

#     # Add auth_provider_x509_cert_url if you want verification on JWTS such as ID tokens
#     GOOGLE_AUTH_PROVIDER_CERT_URL = ""

#     SCOPES = [
#         "https://www.googleapis.com/auth/userinfo.email",
#         "https://www.googleapis.com/auth/userinfo.profile",
#         "openid",
#     ]

#     def __init__(self):
#         self._credentials = google_sdk_login_get_credentials()

#     def _get_redirect_uri(self):
#         domain = settings.BASE_BACKEND_URL
#         api_uri = self.API_URI
#         redirect_uri = f"{domain}{api_uri}"
#         return redirect_uri

#     def _generate_client_config(self):
#         # This follows the structure of the official "client_secret.json" file
#         client_config = {
#             self.GOOGLE_CLIENT_TYPE: {
#                 "client_id": self._credentials.client_id,
#                 "project_id": self._credentials.project_id,
#                 "auth_uri": self.GOOGLE_AUTH_URL,
#                 "token_uri": self.GOOGLE_ACCESS_TOKEN_OBTAIN_URL,
#                 "auth_provider_x509_cert_url": self.GOOGLE_AUTH_PROVIDER_CERT_URL,
#                 "client_secret": self._credentials.client_secret,
#                 "redirect_uris": [self._get_redirect_uri()],
#                 # If you are dealing with single page applications,
#                 # you'll need to set this both in Google API console
#                 # and here.
#                 "javascript_origins": [],
#             }
#         }
#         return client_config

#     # The next step here is to implement get_authorization_url


# # Step 2
# from django.shortcuts import redirect
# from rest_framework.views import APIView


# class PublicApi(APIView):
#     authentication_classes = ()
#     permission_classes = ()


# class GoogleLoginRedirectApi(PublicApi):
#     def get(self, request, *args, **kwargs):
#         google_login_flow = GoogleSdkLoginFlowService()

#         authorization_url, state = google_login_flow.get_authorization_url()

#         request.session["google_oauth2_state"] = state

#         return redirect(authorization_url)


# from rest_framework import serializers, status
# from rest_framework.response import Response


# class GoogleLoginApi(PublicApi):
#     class InputSerializer(serializers.Serializer):
#         code = serializers.CharField(required=False)
#         error = serializers.CharField(required=False)
#         state = serializers.CharField(required=False)

#     def get(self, request, *args, **kwargs):
#         input_serializer = self.InputSerializer(data=request.GET)
#         input_serializer.is_valid(raise_exception=True)

#         validated_data = input_serializer.validated_data

#         code = validated_data.get("code")
#         error = validated_data.get("error")
#         state = validated_data.get("state")

#         if error is not None:
#             return Response(
#                 {"error": error}, status=status.HTTP_400_BAD_REQUEST
#             )

#         if code is None or state is None:
#             return Response(
#                 {"error": "Code and state are required."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         session_state = request.session.get("google_oauth2_state")

#         if session_state is None:
#             return Response(
#                 {"error": "CSRF check failed."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         del request.session["google_oauth2_state"]

#         if state != session_state:
#             return Response(
#                 {"error": "CSRF check failed."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # More code below


# import google_auth_oauthlib.flow
# import requests


# class GoogleSdkLoginFlowService:
#     # Here we have the implementation of get_authorization_url

#     def get_tokens(self, *, code: str, state: str) -> GoogleAccessTokens:
#         redirect_uri = self._get_redirect_uri()
#         client_config = self._generate_client_config()

#         flow = google_auth_oauthlib.flow.Flow.from_client_config(
#             client_config=client_config, scopes=self.SCOPES, state=state
#         )
#         flow.redirect_uri = redirect_uri
#         access_credentials_payload = flow.fetch_token(code=code)

#         if not access_credentials_payload:
#             raise ApplicationError("Failed to obtain tokens from Google.")

#         google_tokens = GoogleAccessTokens(
#             id_token=access_credentials_payload["id_token"],
#             access_token=access_credentials_payload["access_token"],
#         )

#         return google_tokens

#     # More code follows below


# from attrs import define


# @define
# class GoogleAccessTokens:
#     id_token: str
#     access_token: str


# from attrs import define
# import jwt


# @define
# class GoogleAccessTokens:
#     id_token: str
#     access_token: str

#     def decode_id_token(self) -> Dict[str, Any]:
#         id_token = self.id_token
#         decoded_token = jwt.decode(
#             jwt=id_token, options={"verify_signature": False}
#         )
#         return decoded_token
# from typing import Any, Dict
# import requests


# class GoogleSdkLoginFlowService:
# 	# Here we have implemented another methods
#     # See the code snippets above or our Django Styleguide Example.

#     # Reference:
#     # https://developers.google.com/identity/protocols/oauth2/web-server#callinganapi
#     def get_user_info(self, *, google_tokens: GoogleAccessTokens)
#         access_token = google_tokens.access_token

#         response = requests.get(
#             self.GOOGLE_USER_INFO_URL,
#             params={"access_token": access_token}
#         )

#         if not response.ok:
#             raise ApplicationError("Failed to obtain user info from Google.")

#         return response.json()

# from django.contrib.auth import login
# from rest_framework import status
# from rest_framework.response import Response


# # See the implementation of PublicApi class in the previous code snippets.


# class GoogleLoginApi(PublicApi):
# 	# Here we have the serializer class.


#     def get(self, request, *args, **kwargs):
#     	# Here we have made the request validation.

#         google_login_flow = GoogleSdkLoginFlowService()

#         google_tokens = google_login_flow.get_tokens(code=code, state=state)

#         id_token_decoded = google_tokens.decode_id_token()
#         user_info = google_login_flow.get_user_info(google_tokens=google_tokens)

#         user_email = id_token_decoded["email"]
#         user = user_get(email=user_email)

#         if user is None:
#             return Response(
#                 {"error": f"User with email {user_email} is not found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         login(request, user)

#         result = {
#             "id_token_decoded": id_token_decoded,
#             "user_info": user_info,
#         }

#         return Response(result)