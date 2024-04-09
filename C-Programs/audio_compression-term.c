/*
 * Date: 2013-12-16
 * Author: leike@informatik.uni-freiburg.de
 *
 * Simple example for non-termination
 */

extern int __VERIFIER_nondet_int(void);

int main() {
    int x = __VERIFIER_nondet_int();
    int i = 0;
    if (x <= 0) {
        return 0;
    }
    while (x < 1073741824){
        i++;
        x = 2 * x;
    }
	return 0;
}