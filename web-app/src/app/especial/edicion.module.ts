import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedModule } from '../shared/shared.module';
import { EdicionRoutingModule } from './edicion-routing.module';
import { EspecialComponent } from './especial.component';
import { VisualizarComponent } from '../visualizar/visualizar.component';

@NgModule({
  imports: [CommonModule, SharedModule, EdicionRoutingModule],
  declarations: [EspecialComponent, VisualizarComponent],
})
export class EdicionModule {}
