import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CyclingTeamsListComponent } from '../app/cycling-teams-list/cycling-teams-list.component';
import { HomeComponent } from '../app/home/home.component';
import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
  },
  {
    path: 'cycling_teams',
    children: [
      {
        path: '',
        component: CyclingTeamsListComponent,
      },
      {
        path: 'detail',
        loadChildren: () =>
          import('../app/especial/edicion.module').then((m) => m.EdicionModule),
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes), HttpClientModule],
  exports: [RouterModule],
})
export class AppRoutingModule {}
