from sqlalchemy import select

from fast_zero.models import User


def teste_create_user(session):
    # engine = create_engine('sqlite:///database.db')
    # engine = create_engine('sqlite:///:memory:')

    # table_registry.metadata.create_all(engine)
    #
    # with Session(engine) as session:
    user = User(username='username', email='mail@mail.com', password='pass')
    session.add(user)
    session.commit()
    # session.refresh(user)
    result = session.scalar(select(User).where(User.email == 'mail@mail.com'))

    # assert user.id == 1
    assert result.username == 'username'
