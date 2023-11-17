"""add data_id column

Revision ID: 090aece45245
Revises: 38fbc03521de
Create Date: 2023-11-15 21:37:12.495239

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '090aece45245'
down_revision: Union[str, None] = '38fbc03521de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personal_info', sa.Column('data_id', sa.String(length=20), nullable=True))  # noqa:E501
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('personal_info', 'data_id')
    # ### end Alembic commands ###
