from rest_framework_simplejwt.tokens import AccessToken


def get_token(admin):
    access = AccessToken.for_user(admin)

    return {
        "access": str(access.access_token)
    }
    