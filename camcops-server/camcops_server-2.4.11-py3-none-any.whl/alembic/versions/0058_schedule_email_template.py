#!/usr/bin/env python

"""
camcops_server/alembic/versions/0058_schedule_email_template.py

===============================================================================

    Copyright (C) 2012-2020 Rudolf Cardinal (rudolf@pobox.com).

    This file is part of CamCOPS.

    CamCOPS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CamCOPS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CamCOPS. If not, see <https://www.gnu.org/licenses/>.

===============================================================================

DATABASE REVISION SCRIPT

schedule_email_template

Revision ID: 0058
Revises: 0057
Creation date: 2021-03-11 11:13:07.146799

"""

# =============================================================================
# Imports
# =============================================================================

from alembic import op
import sqlalchemy as sa


# =============================================================================
# Revision identifiers, used by Alembic.
# =============================================================================

revision = '0058'
down_revision = '0057'
branch_labels = None
depends_on = None


# =============================================================================
# The upgrade/downgrade steps
# =============================================================================

# noinspection PyPep8,PyTypeChecker
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('_task_schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email_subject', sa.UnicodeText(),
                                      nullable=False, comment='email subject'))
        batch_op.add_column(sa.Column('email_template', sa.UnicodeText(),
                                      nullable=False, comment='email template'))


# noinspection PyPep8,PyTypeChecker
def downgrade():
    with op.batch_alter_table('_task_schedule', schema=None) as batch_op:
        batch_op.drop_column('email_subject')
        batch_op.drop_column('email_template')
