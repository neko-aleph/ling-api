from db.repos.sqlalchemy_repo import SqlAlchemyRepository


class Service:
    def __init__(self, repo: SqlAlchemyRepository):
        self.repo = repo

    def add(self, entity):
        return self.repo.add(entity)

    def remove(self, id: int):
        return self.repo.delete(id)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get(id)

    def update(self, id, entity):
        return self.repo.update(id, entity)