AItools = [
    {
        "type": "function",
        "function": {
            "name": "calculateMean",
            "description": "Calculate the mean of a given column in a CSV file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column for which the mean should be calculated. It should contain only numeric values.",
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
            "name": "calculateMedian",
            "description": "Calculate the median of a given column in a CSV file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column for which the median should be calculated. It should contain only numeric values.",
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
            "description": "Calculate the mode (most frequent value) of a given column in a CSV file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column for which the mode should be calculated. It should contain only numeric values.",
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
            "description": "Calculate the variance of a given column in a CSV file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column for which the variance should be calculated. It should contain only numeric values.",
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
            "description": "Calculate the standard deviation of a given column in a CSV file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column for which the standard deviation should be calculated. It should contain only numeric values.",
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
            "description": "Count the number of data rows in the CSV file (excluding the header row).",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "getColumnInfo",
            "description": "Get detailed information about a specific column, including its data type, unique values, missing values, and basic statistics if numeric. For non-numeric columns, shows the most common values.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column to analyze",
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
            "description": "Generates a histogram visualization from a column of numeric data, showing the distribution of values. Uses Sturges' formula (k = 1 + log2(n)) to calculate optimal bin count if not specified. The graph is automatically emitted to all connected clients.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column to visualize (must contain numeric values)"
                    },
                    "xaxis": {
                        "type": "string",
                        "description": "Label for the x-axis"
                    },
                    "yaxis": {
                        "type": "string",
                        "description": "Label for the y-axis"
                    },
                    "title": {
                        "type": "string",
                        "description": "Title of the histogram"
                    },
                    "density": {
                        "type": "boolean",
                        "description": "Whether to normalize the histogram (optional, defaults to false)"
                    },
                    "normal_dist": {
                        "type": "boolean",
                        "description": "Whether to overlay a normal distribution curve (optional, defaults to false)"
                    },
                    "histobin": {
                        "type": "integer",
                        "description": "Number of bins for the histogram (optional, if not specified uses Sturges' formula: k = 1 + log2(n))"
                    }
                },
                "required": ["colName", "xaxis", "yaxis", "title"],
                "additionalProperties": False,
            },
            "strict": False,
        },
    },
]
