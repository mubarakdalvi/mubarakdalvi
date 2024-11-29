import { CanMatchFn } from '@angular/router';

export const matchGuard: CanMatchFn = (route, segments) => {
  return true;
};
