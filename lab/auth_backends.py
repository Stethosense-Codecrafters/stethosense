from django.contrib.auth import get_user_model
from lab.models import LabUser

CustomUser = get_user_model()

class LabUserBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            # First, check if the login request is for a regular user
            try:
                user = CustomUser.objects.get(email=username)
                if user.check_password(password):
                    return user
            except CustomUser.DoesNotExist:
                pass

            # If not a regular user, it could be a lab user with lab ID
            try:
                lab_user = LabUser.objects.get(lab_id=username)
                if lab_user.lab_password == password:
                    return lab_user
            except LabUser.DoesNotExist:
                return None

        except CustomUser.DoesNotExist:
            # The username is not a regular user's email; it could be a lab ID
            try:
                lab_user = LabUser.objects.get(lab_id=username)
                if lab_user.lab_password == password:
                    return lab_user
            except LabUser.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            try:
                return LabUser.objects.get(pk=user_id)
            except LabUser.DoesNotExist:
                return None
