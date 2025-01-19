AItools = [
    {
        "type": "function",
        "function": {
            "name": "calculateMean",
            "description": "Calculate the arithmetic mean (average) of a numeric column. Returns a floating point number representing the mean, or an error message string if the column contains non-numeric values. When exclude_outliers is true, removes statistical outliers (values beyond 1.5 times the interquartile range from Q1 and Q3) before calculating the mean. Example return values: 42.5 (success) or 'Error: Column 'xyz' contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column as it appears in the CSV header. Must match case. Example: 'Age' or 'SalesAmount'",
                    },
                    "exclude_outliers": {
                        "type": "boolean",
                        "description": "When true, removes statistical outliers before calculating mean. When false or omitted, uses all values.",
                    },
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": False,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateMedian",
            "description": "Calculate the median (middle value) of a numeric column. Returns a floating point number representing the median, or an error message if the column contains non-numeric values. For even-length datasets, returns the average of the two middle values. Example return values: 35.5 (success) or 'Error: Column 'xyz' contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column as it appears in the CSV header. Must match case. Example: 'Age' or 'Price'",
                    }
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateMode",
            "description": "Calculate the mode (most frequent value) of a column with numerical values only. Returns the mode as a string, or multiple modes if there are ties. Special cases: 'No mode - all values appear once' when all values are unique, or an error message for invalid data. Example returns: '42', 'Multiple modes: 10, 20, 30', or 'Error: Column contains non-numeric values'.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column as it appears in the CSV header. Must match case. Example: 'Category' or 'Rating'",
                    }
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateVariance",
            "description": "Calculate the statistical variance (average squared deviation from the mean) of a numeric column. Returns a floating point number, or an error message for non-numeric data. Example returns: 156.7 (success) or 'Error: Column contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column as it appears in the CSV header. Must match case. Example: 'Temperature' or 'Score'",
                    }
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateStandardDeviation",
            "description": "Calculate the standard deviation (square root of variance) of a numeric column. Returns a floating point number representing the spread of data, or an error message for non-numeric data. Example returns: 12.5 (success) or 'Error: Column contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column as it appears in the CSV header. Must match case. Example: 'Height' or 'Weight'",
                    }
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "countRows",
            "description": "Count the total number of data rows in the CSV file, excluding the header row. Returns a positive integer. Example return: 1000",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "getColumnInfo",
            "description": "Analyze a column and return detailed statistics and information. For numeric columns: shows data type, count, unique values, missing values, min, max, and mean. For categorical columns: shows data type, count, unique values, missing values, and top 3 most common values. Example return: 'Column 'Age' analysis:\n- Data type: float64\n- Total values: 1000\n- Unique values: 50\n- Missing values: 0\n- Minimum value: 18\n- Maximum value: 80\n- Average value: 42.5'",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column to analyze as it appears in the CSV header. Must match case.",
                    }
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "searchValue",
            "description": "Search for a specific value across all columns in the data. Returns the number of matches per column and example matching values. This is useful for finding where certain values appear in the dataset.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The value to search for in the data",
                    }
                },
                "required": ["query"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "searchRowDetails",
            "description": "Search for rows where a specific column contains the query value and return detailed information about those rows. Optional: specify 'limit' to control how many matches to show (defaults to 5 if not specified).",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The column to search in",
                    },
                    "query": {
                        "type": "string",
                        "description": "The value to search for",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of matching rows to show in detail (optional, defaults to 5)",
                    },
                },
                "required": ["colName", "query"],
                "additionalProperties": False,
            },
            "strict": False,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "bargraphToImage",
            "description": "Generates a bar graph visualization from a column of data, showing the frequency or count of each unique value. The graph is automatically emitted to all connected clients.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column to visualize",
                    },
                    "xaxis": {"type": "string", "description": "Label for the x-axis"},
                    "yaxis": {"type": "string", "description": "Label for the y-axis"},
                    "title": {
                        "type": "string",
                        "description": "Title of the bar graph",
                    },
                },
                "required": ["colName", "xaxis", "yaxis", "title"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "histoToImage",
            "description": "Generates and emits a histogram visualization from numeric data. Returns a success/error message string. The histogram image is automatically sent to connected clients via WebSocket. Supports density normalization and normal distribution overlay. Example return: 'Successfully generated and emitted histogram for column 'Age'' or 'Error: Column contains non-numeric values'",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The exact name of the column as it appears in the CSV header. Must contain numeric values. Example: 'Age' or 'Income'",
                    },
                    "xaxis": {
                        "type": "string",
                        "description": "Label text for the x-axis. Example: 'Age (years)' or 'Income ($)'",
                    },
                    "yaxis": {
                        "type": "string",
                        "description": "Label text for the y-axis. Example: 'Frequency' or 'Count'",
                    },
                    "title": {
                        "type": "string",
                        "description": "Title text for the histogram. Example: 'Age Distribution' or 'Income Spread'",
                    },
                    "density": {
                        "type": "boolean",
                        "description": "When true, normalizes the histogram to show density instead of counts",
                    },
                    "normal_dist": {
                        "type": "boolean",
                        "description": "When true, overlays a normal distribution curve on the histogram",
                    },
                    "histobin": {
                        "type": "integer",
                        "description": "Number of bins for the histogram. If omitted, uses Sturges' formula: k = 1 + log2(n)",
                    },
                },
                "required": ["colName", "xaxis", "yaxis", "title"],
                "additionalProperties": False,
            },
            "strict": False,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "colNameToPiechart",
            "description": "Generates a pie chart visualization from a column of data, showing the proportion of each unique value. The chart is automatically emitted to all connected clients.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column to visualize",
                    },
                    "title": {
                        "type": "string",
                        "description": "Title of the pie chart",
                    },
                },
                "required": ["colName", "title"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_filtered_results_from_string",
            "description": "Fetches a list of values from a target column in a CSV string based on a specific filter applied to another column.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query_param": {
                        "type": "string",
                        "description": "The column name to apply the filter on.",
                    },
                    "query_value": {
                        "type": "string",
                        "description": "The value to filter the rows by in the query column.",
                    },
                    "target_param": {
                        "type": "string",
                        "description": "The column name to retrieve values from based on the filter.",
                    },
                },
                "required": ["query_param", "query_value", "target_param"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "listToPiechart",
            "description": "Generates a pie chart image from the provided data list and emits the image via WebSocket to all connected clients. Can be used in conjunction with get_filtered_results_from_string",
            "parameters": {
                "type": "object",
                "properties": {
                    "valSet": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "A list of all the values, under the specific head. list repeats values to count occurences",
                    },
                    "title": {
                        "type": "string",
                        "description": "The title of the pie chart.",
                    },
                },
                "required": ["valSet", "title"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "correlationAnalysis",
            "description": "Analyzes correlation between two numeric columns and generates a scatter plot. Returns a string containing the correlation coefficient and emits the plot image via WebSocket. Example return: 'Correlation coefficient between Height and Weight: 0.856' or 'Error: Columns contain non-numeric values'",
            "parameters": {
                "type": "object",
                "properties": {
                    "col1": {
                        "type": "string",
                        "description": "First column name exactly as it appears in CSV header. Must be numeric. Example: 'Height'",
                    },
                    "col2": {
                        "type": "string",
                        "description": "Second column name exactly as it appears in CSV header. Must be numeric. Example: 'Weight'",
                    },
                    "title": {
                        "type": "string",
                        "description": "Title for the scatter plot. Example: 'Height vs Weight Correlation'",
                    },
                    "show_trend": {
                        "type": "boolean",
                        "description": "When true, displays a trend line on the scatter plot. Defaults to true",
                    },
                },
                "required": ["col1", "col2", "title"],
                "additionalProperties": False,
            },
            "strict": False,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateMeanfromList",
            "description": "Calculate the arithmetic mean of a list of numbers. Returns a float or error message. Handles outlier exclusion similar to calculateMean. Example returns: 42.5 (success) or 'Error: List contains non-numeric values' (failure)",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of numeric values as strings. Example: ['1.5', '2.0', '3.5']",
                    },
                    "exclude_outliers": {
                        "type": "boolean",
                        "description": "When true, removes values beyond 1.5 IQR from quartiles before calculating",
                    },
                },
                "required": ["data"],
                "additionalProperties": False,
            },
            "strict": False,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateMedianfromList",
            "description": "Calculate the median (middle value) of a list of numbers. Returns a float or error message. For even-length lists, returns average of two middle values. Example returns: 23.5 (success) or 'Error: List contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of numeric values as strings. Example: ['20', '23', '25', '28']",
                    }
                },
                "required": ["data"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateModefromList",
            "description": "Calculate the mode (most frequent value) of a list. Returns the mode as a string, or describes multiple modes if present. Example returns: '42', 'Multiple modes: 10, 20, 30', or 'No mode - all values appear once' for unique values.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of values to analyze. Example: ['red', 'blue', 'red', 'green']",
                    }
                },
                "required": ["data"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateVariancefromList",
            "description": "Calculate the statistical variance (average squared deviation from mean) of a list. Returns a float or error message. Example returns: 156.7 (success) or 'Error: List contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of numeric values as strings. Example: ['10.5', '12.3', '15.7']",
                    }
                },
                "required": ["data"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculateStandardDeviationfromList",
            "description": "Calculate the standard deviation (square root of variance) of a list. Returns a float or error message. Example returns: 12.5 (success) or 'Error: List contains non-numeric values' (failure).",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of numeric values as strings. Example: ['100', '120', '140']",
                    }
                },
                "required": ["data"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "bargraphToImagefromList",
            "description": "Generate and emit a bar graph visualization from a list of values. Returns a success/error message string and automatically sends the graph image via WebSocket. Example return: 'Successfully generated and emitted bar graph' or 'Error generating bar graph: Invalid data'",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of values to visualize. Can be numeric or categorical. Example: ['A', 'B', 'A', 'C']",
                    },
                    "xaxis": {
                        "type": "string",
                        "description": "Label for x-axis. Example: 'Categories' or 'Product Types'",
                    },
                    "yaxis": {
                        "type": "string",
                        "description": "Label for y-axis. Example: 'Frequency' or 'Count'",
                    },
                    "title": {
                        "type": "string",
                        "description": "Title of the graph. Example: 'Distribution of Product Types'",
                    },
                },
                "required": ["data", "xaxis", "yaxis", "title"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
]
