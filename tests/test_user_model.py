from api.models import User
from pytest import raises


class TestUserModel:
    """Test user model """

    def test_save_model(self, set_db, new_user):
        """should save model"""
        new_user.save()
        assert User.query.count() == 1

    def test_delete_model(self, set_db, new_user):
        """ should delete model"""
        new_user.save()
        new_user.delete()
        assert User.query.get(new_user.id) == None

    def test_get_password_fails(self, set_db, new_user):
        """should raise Attribute when reading attribute"""
        new_user.save()
        with raises(AttributeError) as error:
            password = new_user.password
        assert 'Password is not a readable attribute' in str(error)

    def test_generate_token(self, set_db, new_user):
        """Should generate user token"""
        new_user.save()
        token = new_user.generate_token()
        assert token is not None

    def test_verify_token(self, set_db, new_user):
        """Should verify user token """
        new_user.save()
        token = new_user.generate_token()
        user = new_user.verify_token(token)
        assert user.id == new_user.id
