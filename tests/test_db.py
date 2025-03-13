from sqlalchemy import select

from fast_zero_course.models import User


def test_create_user(session):
    user = User(
        username='rojo',
        email='rojo@gmail.com',
        password='dragao',
    )

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'rojo@gmail.com'))

    assert result.id == 1
