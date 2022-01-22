"""Initial migration

Revision ID: 0001
Revises:
Create Date: 2022-01-23 01:26:51.684615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "channel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(length=255), nullable=False),
        sa.Column("start_listen_at", sa.Boolean(), nullable=True),
        sa.Column("ping_listen_at", sa.Boolean(), nullable=True),
        sa.Column("stop_listen_at", sa.Boolean(), nullable=True),
        sa.Column("ignore", sa.Boolean(), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("channel")
    # ### end Alembic commands ###
