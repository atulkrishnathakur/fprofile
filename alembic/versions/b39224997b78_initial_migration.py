"""Initial migration

Revision ID: b39224997b78
Revises: 
Create Date: 2024-04-18 11:24:21.718303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b39224997b78'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_countries_id'), 'countries', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_countries_id'), table_name='countries')
    op.drop_table('countries')
    # ### end Alembic commands ###
