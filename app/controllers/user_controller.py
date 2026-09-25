from app.services.user_service import UserService
from app.utils.response import api_response

class UserController:
    @staticmethod
    def get_statistics():
        data = UserService.get_user_statistics()
        return api_response(200, True, 'Statistics fetched successfully', data)

    @staticmethod
    def create_user():
        return api_response(201, True, 'User created successfully', {})

    @staticmethod
    def get_all_users():
        return api_response(200, True, 'Users fetched', [])

    @staticmethod
    def get_user_by_id(user_id):
        return api_response(200, True, 'User fetched', {})

    @staticmethod
    def delete_user(user_id):
        return api_response(200, True, 'User deleted', {})

    @staticmethod
    def update_user_profile(user_id):
        return api_response(200, True, 'Profile updated', {})

    @staticmethod
    def filter_users():
        return api_response(200, True, 'Filtered users', [])