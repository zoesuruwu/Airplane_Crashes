column_defs = [
    {"headerName": "Year", "field": "year", "width": 100},  # Width set to 150
    {
        "headerName": "Date",
        "field": "Date",
        "filter": "agDateColumnFilter",
        "width": 100,
        "filterParams": {
            "comparator": {"function": "dateFilterComparator"},
        },
    },
    {"headerName": "Location", "field": "Location", "width": 150},
    {"headerName": "Operator", "field": "Operator", "width": 150},
    {"headerName": "Type", "field": "Type", "width": 150},
    {"headerName": "Aboard", "field": "Aboard", "width": 100},  # Width set to 200
    {
        "headerName": "Fatalities",
        "field": "Fatalities",
        "width": 100,
    },
    {
        "headerName": "Summary",
        "field": "Summary",
        "wrapText": True,  # Enable text wrapping
        "autoHeight": True,  # Enable auto row height
        "flex": 1,  # Adjust the column width as needed
    },
    {"headerName": "Main cause", "field": "main_cause", "width": 100},
]

column_defs_reasons = [
    {"headerName": "Year", "field": "year", "width": 100},  # Width set to 150
    {
        "headerName": "Date",
        "field": "Date",
        "filter": "agDateColumnFilter",
        "width": 100,
        "filterParams": {
            "comparator": {"function": "dateFilterComparator"},
        },
    },
    {"headerName": "Location", "field": "Location", "width": 150},
    {"headerName": "Operator", "field": "Operator", "width": 150},
    {"headerName": "Type", "field": "Type", "width": 150},
    {"headerName": "Aboard", "field": "Aboard", "width": 100},  # Width set to 200
    {
        "headerName": "Fatalities",
        "field": "Fatalities",
        "width": 100,
    },
    {
        "headerName": "Summary",
        "field": "Summary",
        "wrapText": True,  # Enable text wrapping
        "autoHeight": True,  # Enable auto row height
        "flex": 1,  # Adjust the column width as needed
    },
]
