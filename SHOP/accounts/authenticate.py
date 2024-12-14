from accounts.models import User


class PhoneBackend:
    def authenticate(self,phone_number=None, password=None):
        try:
            user = User.objects.get(phone_number = phone_number)
            if password:
                if user.check_password(password):
                    return user
                else:
                    return None
            return user
        except User.objects.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.objects.DoesNoteExist:
            return None

