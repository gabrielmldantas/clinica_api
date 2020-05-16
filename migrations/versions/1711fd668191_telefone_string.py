"""Telefone string

Revision ID: 1711fd668191
Revises: 7c8e8e5aa2f7
Create Date: 2020-05-13 14:04:41.137254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1711fd668191'
down_revision = '7c8e8e5aa2f7'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('paciente', 'telefone',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=20),
               existing_nullable=False)


def downgrade():
    op.alter_column('paciente', 'telefone',
               existing_type=sa.String(length=20),
               type_=sa.INTEGER(),
               existing_nullable=False)
