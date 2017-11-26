import math
import scipy.stats


def conversion_rate(test):
    return test[1] / test[0]


def conversion_rate_uncertainty(test):
    c = conversion_rate(test)
    return math.sqrt((c * (1 - c)) / test[0])


def conversion_uplift(control, test):
    c = conversion_rate(control)
    t = conversion_rate(test)
    return (t-c)/c


def z_score(test, test_unc, control, control_unc):
    return (test - control) / math.sqrt(test_unc**2 + control_unc**2)


def p_value(z_score):
    return scipy.stats.norm.sf(abs(z_score))


def ab_test(control, *args, p=0.05):
    conversion_rate_c = conversion_rate(control)
    conversion_rate_cu = conversion_rate_uncertainty(control)
    print('CONTROL:')
    print('conversion rate:\t{0} ± {1}'.format(round(conversion_rate_c, 4),
                                                round(conversion_rate_cu, 4)))
    print('threshhold p-value:\t{0}\n'.format(p))

    for i, test in enumerate(args):
        conversion_rate_t = conversion_rate(test)
        conversion_rate_tu = conversion_rate_uncertainty(test)

        uplift = conversion_uplift(control, test)

        Z = z_score(conversion_rate_t, conversion_rate_tu,
                    conversion_rate_c, conversion_rate_cu)

        P = p_value(Z)

        better_than_control = True if uplift > 0 else False
        significant_test = True if P < p else False

        print((80*'-' + '\nTEST {}\n' + 80*'-') .format(i+1))

        if not significant_test:
            print('We can\'t say anything significant '
                  'about how well the test performed')

        if significant_test and better_than_control:
            print('The test performed better than the '
                  'control by a significant margin!')

        if significant_test and not better_than_control:
            print('The test performed worse than the '
                  'control by a significant margin.')

        print('conversion rate:\t{} ± {}'.format(round(conversion_rate_t, 4),
                                                  round(conversion_rate_tu, 4)))
        print('uplift:\t\t\t' + str(round(uplift, 4)))
        print('Z-score:\t\t' + str(round(Z, 4)))
        print('p-value:\t\t' + str(round(P, 4)))
        print()
