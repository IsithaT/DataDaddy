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
                        "description": "The name of the column for which the mean should be calculated.",
                    }
                },
                "required": ["colName"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]
