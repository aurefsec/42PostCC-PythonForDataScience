def callLimit(limit: int):
    """Decorator that limits the number of calls of decorated function"""

    count = 0

    def callLimiter(function):
        """Decorator that wrap function to limits the number of exec"""

        def limit_function(*args: any, **kwds: any):
            """Wrapper that exec the function only if count < limit"""

            nonlocal count

            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(function, "call to many times")

        return limit_function

    return callLimiter
