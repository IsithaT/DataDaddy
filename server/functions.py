AItools = [
    {
        "type": "function",
        "function": {
            "name": "calculateMean",
            "description": "Calculate the mean of a given column in a CSV file. Can optionally exclude outliers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "colName": {
                        "type": "string",
                        "description": "The name of the column for which the mean should be calculated. It should contain only numeric values.",
                    },
                    "exclude_outliers": {
                        "type": "boolean",
                        "description": "Whether to exclude statistical outliers (values beyond 1.5 IQR). Defaults to false."
                    }
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
            "description": "Generates a histogram visualization from a column of numeric data. The graph is automatically emitted to all connected clients.",
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
                        "description": "Number of bins for the histogram (optional, if not specified uses Sturges' formula)"
                    },
                    "color": {
                        "type": "string",
                        "description": "Color for the histogram bars (optional, defaults to system color)"
                    }
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
                        "description": "The name of the column to visualize"
                    },
                    "title": {
                        "type": "string",
                        "description": "Title of the pie chart"
                    }
                },
                "required": ["colName", "title"],
                "additionalProperties": False
            },
            "strict": True
        }
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
          "description": "The column name to apply the filter on."
        },
        "query_value": {
          "type": "string",
          "description": "The value to filter the rows by in the query column."
        },
        "target_param": {
          "type": "string",
          "description": "The column name to retrieve values from based on the filter."
        }
      },
      "required": ["query_param", "query_value", "target_param"],
      "additionalProperties": False
    },
    "strict": True
  }
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
          "items": {
            "type": "string"
          },
          "description": "A list of all the values, under the specific head. list repeats values to count occurences"
        },
        "title": {
          "type": "string",
          "description": "The title of the pie chart."
        }
      },
      "required": ["valSet", "title"],
      "additionalProperties": False
    },
    "strict": True
  }
},

{
    "type": "function",
    "function": {
        "name": "correlationAnalysis",
        "description": "Analyze correlation between two numeric columns and generate a scatter plot with optional trend line.",
        "parameters": {
            "type": "object",
            "properties": {
                "col1": {
                    "type": "string",
                    "description": "First column name (numeric values)"
                },
                "col2": {
                    "type": "string",
                    "description": "Second column name (numeric values)"
                },
                "title": {
                    "type": "string",
                    "description": "Title for the scatter plot"
                },
                "show_trend": {
                    "type": "boolean",
                    "description": "Whether to show trend line (optional, defaults to true)"
                }
            },
            "required": ["col1", "col2", "title"],
            "additionalProperties": False
        },
        "strict": False
    }
},
    {
        "type": "function",
        "function": {
            "name": "calculateMeanfromList",
            "description": "Calculate the mean of a given list of numbers. Can optionally exclude outliers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The list of numbers to calculate the mean from",
                    },
                    "exclude_outliers": {
                        "type": "boolean",
                        "description": "Whether to exclude statistical outliers (values beyond 1.5 IQR). Defaults to false."
                    }
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
            "description": "Calculate the median of a given list of numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The list of numbers to calculate the median from",
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
            "description": "Calculate the mode (most frequent value) of a given list of numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The list of numbers to calculate the mode from",
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
            "description": "Calculate the variance of a given list of numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The list of numbers to calculate the variance from",
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
            "description": "Calculate the standard deviation of a given list of numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The list of numbers to calculate the standard deviation from",
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
            "description": "Generates a bar graph visualization from a list of values, showing the frequency or count of each unique value. The graph is automatically emitted to all connected clients.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The list of values to visualize",
                    },
                    "xaxis": {"type": "string", "description": "Label for the x-axis"},
                    "yaxis": {"type": "string", "description": "Label for the y-axis"},
                    "title": {
                        "type": "string",
                        "description": "Title of the bar graph",
                    },
                },
                "required": ["data", "xaxis", "yaxis", "title"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
]
