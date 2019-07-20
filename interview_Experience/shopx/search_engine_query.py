
def run_testcase():
    """
    Take the input for the testcase and execute
    """
    queries_count = {}
    for i in range(0, int(input())):
        query = input()
        if query.startswith('top'):
            query_parts = query.split(' ')

            requested_count = int(query_parts[1])
            # use negative value so that highest will be first in sort
            sort_key = lambda x:(-x[1],x[0])
            items = [item[0] for item in sorted(list(queries_count.items()), key=sort_key)[:requested_count]]
            print(' '.join(items))
        else:
            if query not in queries_count:
                queries_count[query] = 1
            else:
                queries_count[query] += 1

if __name__ == "__main__":
    for tc in range(0, int(input())):
        run_testcase()