# http://www.aup.ru/books/m157/4_3_3.htm

from math import sqrt


prod_all = 24000
monthly_storing = 0.1
one_batch_cost = 350
planning_time = 365


def get_daily_norm(amount_of_all_product, days):
    return amount_of_all_product / days


def get_daily_storing(monthly_storing_cost):
    return monthly_storing_cost * 12 / 365


def get_q0(daily_norm, daily_storing, cost_of_one_batch):
    return sqrt(2 * daily_norm * cost_of_one_batch / daily_storing)


def get_qn(daily_norm, all_time, n):
    return daily_norm * all_time / n


# average costs function
def f(daily_norm, cost_of_one_batch, daily_storing, q):
    return (daily_norm * cost_of_one_batch / q) + (daily_storing * q / 2)


def main():
    daily_norm = get_daily_norm(prod_all, planning_time)
    daily_storing = get_daily_storing(monthly_storing)
    q0 = get_q0(daily_norm, daily_storing, one_batch_cost)
    q_next = 0
    q_prev = 0
    n = 1
    while not (q_prev >= q0 > q_next):
        q_prev = q_next
        q_next = get_qn(daily_norm, prod_all, n)
        n += 1
    f_next = f(daily_norm, one_batch_cost, daily_storing, q_next)
    f_prev = f(daily_norm, one_batch_cost, daily_storing, q_prev)
    optimal_batch_size = q_next if f_next < f_prev else q_prev
    optimal_interval = planning_time / (prod_all / optimal_batch_size)
    print('Optimal batch size: {0}'.format(optimal_batch_size))
    print('Optimal interval: {0}'.format(optimal_interval))


if __name__ == '__main__':
    main()
