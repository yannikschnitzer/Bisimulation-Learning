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

    if (x > y) {
        return 0;
    }

    while (x >= 0){
        if (x <= y) {
            x = x - 1;
        } 
    }
	return 0;
}