/*
 * Date: 2013-12-16
 * Author: leike@informatik.uni-freiburg.de
 *
 * Simple example for non-termination
 */

extern int __VERIFIER_nondet_int(void);

int main() {
    int x = __VERIFIER_nondet_int();

    while (x < 10000){
        x = x * x * x;
    }

	return 0;
}
