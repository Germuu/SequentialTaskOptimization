

def check_condition(T, max_node_time):
    total_time = sum(T)
    return (total_time - max_node_time) < (total_time / 2)


def calculate_bottom_50_mean(mean, std_dev):
    return mean - (0.7978847 * std_dev)


def optimize_process(T, max_node_sd):
    max_node_time = max(T)

    if not check_condition(T, max_node_time):
        print("Condition not satisfied, optimization will not work.")
        return sum(T)

    optimized_max_time = calculate_bottom_50_mean(max_node_time, max_node_sd)
    

    return optimized_max_time


T = [ 11,2,3,2,2]
max_node_sd = 3
n_workers = 10

optimized_value = optimize_process(T, max_node_sd)
total_path = sum(T) - max(T)
result = max(optimized_value, total_path)

original_cars_per_hour = (60 / sum(T)) * n_workers
optimized_cars_per_hour = (60 / result * (n_workers / 2))

print(f"optimized max node = {optimized_value}")
print(f"Original cars per hour = {original_cars_per_hour}")
print(f"Optimized cars per hour = {optimized_cars_per_hour}")
