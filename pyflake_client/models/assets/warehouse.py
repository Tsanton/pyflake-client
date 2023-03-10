"""warehouse"""
# pylint: disable=line-too-long
from dataclasses import dataclass
from pyflake_client.models.assets.database import Database
from pyflake_client.models.assets.snowflake_asset_interface import ISnowflakeAsset


@dataclass(frozen=True)
class Warehouse(ISnowflakeAsset):
    """Warehouse"""
    warehouse_name: str
    comment: str
    size: str = "XSMALL" #TODO: Enum
    warehouse_type: str = "STANDARD"
    auto_resume: bool = True
    auto_suspend: int = 30
    init_suspend: bool = True
    owner: str = "SYSADMIN"

    def get_create_statement(self):
        """get_create_statement"""
        return f"""CREATE OR REPLACE WAREHOUSE {self.warehouse_name} WITH WAREHOUSE_SIZE = '{self.size}' WAREHOUSE_TYPE = '{self.warehouse_type}' AUTO_RESUME = {self.auto_resume} AUTO_SUSPEND = {self.auto_suspend} INITIALLY_SUSPENDED = {self.init_suspend} COMMENT = '{self.comment}';
                   GRANT OWNERSHIP ON WAREHOUSE {self.warehouse_name} to {self.owner} REVOKE CURRENT GRANTS;"""

    def get_delete_statement(self):
        """get_delete_statement"""
        return f"DROP WAREHOUSE IF EXISTS {self.warehouse_name};"
