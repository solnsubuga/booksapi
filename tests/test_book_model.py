from api.models import Book
from pytest import raises


class TestBookModel:
    """Test book model """

    def test_save_model(self, set_db, new_book):
        """should save book"""
        new_book.save()
        assert Book.query.count() == 1

    def test_delete_model(self, set_db, new_book):
        """ should delete book"""
        new_book.save()
        new_book.delete()
        assert Book.query.get(new_book.id) == None
