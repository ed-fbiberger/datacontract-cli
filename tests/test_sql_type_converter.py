from open_data_contract_standard.model import SchemaProperty

from datacontract.export.sql_type_converter import convert_to_sql_type


def test_odcs_physical_type_returned_directly():
    prop = SchemaProperty(name="order_total", logicalType="number", physicalType="DECIMAL(38,2)")
    assert convert_to_sql_type(prop, "postgres") == "DECIMAL(38,2)"
    assert convert_to_sql_type(prop, "snowflake") == "DECIMAL(38,2)"
    assert convert_to_sql_type(prop, "databricks") == "DECIMAL(38,2)"


def test_odcs_logical_type_used_when_no_physical_type():
    prop = SchemaProperty(name="order_total", logicalType="number")
    result = convert_to_sql_type(prop, "postgres")
    assert result == "numeric"


def test_odcs_physical_type_takes_precedence():
    prop = SchemaProperty(name="order_total", logicalType="number", physicalType="DECIMAL(38,2)")
    result = convert_to_sql_type(prop, "postgres")
    assert result == "DECIMAL(38,2)"
