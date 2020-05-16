"""Criacao da tabela consulta

Revision ID: d272b3ce18b6
Revises: 7e0e834e6151
Create Date: 2020-05-16 16:41:38.843481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd272b3ce18b6'
down_revision = '7e0e834e6151'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('consulta',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('data', sa.Date(), nullable=False),
        sa.Column('id_medico', sa.Integer(), nullable=False),
        sa.Column('id_paciente', sa.Integer(), nullable=False),
        sa.Column('id_cobertura', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_cobertura'], ['cobertura.id'], ),
        sa.ForeignKeyConstraint(['id_medico'], ['medico.id'], ),
        sa.ForeignKeyConstraint(['id_paciente'], ['paciente.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('consulta')
