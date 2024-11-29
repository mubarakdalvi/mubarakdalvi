import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard', //login
    pathMatch: 'full', // Default route will alway redirect to header
  },
  {
    path: '',
    loadChildren: () =>
      import('./main/main.module').then((mod) => mod.MainModule), //lazy loading done with this only needed will load , which make app faster
  },
  {
    path: 'authorize',
    loadChildren: () =>
      import('./authorize/authorize.module').then((mod) => mod.AuthorizeModule), //lazy loading done with this only needed will load , which make app faster
  },
  {
    path: 'register',
    loadChildren: () =>
      import('./register/register.module').then((mod) => mod.RegisterModule), //lazy loading done with this only needed will load , which make app faster
  },

  { path: '**', redirectTo: 'dashboard' }, // Wildcard route always add this at ending for this to tyry every route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
