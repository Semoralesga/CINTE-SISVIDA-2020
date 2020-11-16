import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EspecialComponent } from './especial.component';

const routes: Routes = [
  {
    path: '',
    component: EspecialComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class EdicionRoutingModule {}
