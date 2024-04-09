/*
 * Date: 2013-12-16
 * Author: leike@informatik.uni-freiburg.de
 *
 * Simple example for non-termination
 */

extern int __VERIFIER_nondet_int(void);

int main() {
    int x = __VERIFIER_nondet_int();
    int y = __VERIFIER_nondet_int();

    if (x <= 0 | y <= 0){
        return 0;
    }

    while (x != y){
        if (x > y) {
            x = x - y;
        } else {
            y = y - x;
        }
    }
	return 0;
}