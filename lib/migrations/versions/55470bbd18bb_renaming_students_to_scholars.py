"""Renaming students to scholars

Revision ID: 55470bbd18bb
Revises: 791279dd0760
Create Date: 2023-09-02 09:38:48.254164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55470bbd18bb'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
