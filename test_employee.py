from employee import employee_details


def test_employee_details():
    result = employee_details("Keerti", "EMP101", "IT", "30000")

    expected = "Name: Keerti\nEmployee ID: EMP101\nDepartment: IT\nSalary: 30000"

    assert result == expected