"""Initial migration remove state

Revision ID: 391ce120c338
Revises: 3055a56f6f1c
Create Date: 2024-04-03 11:15:36.263921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '391ce120c338'
down_revision: Union[str, None] = '3055a56f6f1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_states_id', table_name='states')
    op.drop_table('states')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('states',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('state_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('country_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='states_pkey')
    )
    op.create_index('ix_states_id', 'states', ['id'], unique=False)
    # ### end Alembic commands ###
