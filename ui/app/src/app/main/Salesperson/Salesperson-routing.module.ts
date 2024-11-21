import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SalespersonHomeComponent } from './home/Salesperson-home.component';
import { SalespersonNewComponent } from './new/Salesperson-new.component';
import { SalespersonDetailComponent } from './detail/Salesperson-detail.component';

const routes: Routes = [
  {path: '', component: SalespersonHomeComponent},
  { path: 'new', component: SalespersonNewComponent },
  { path: ':id', component: SalespersonDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Salesperson-detail-permissions'
      }
    }
  },{
    path: ':salesperson_id/Sale', loadChildren: () => import('../Sale/Sale.module').then(m => m.SaleModule),
    data: {
        oPermission: {
            permissionId: 'Sale-detail-permissions'
        }
    }
}
];

export const SALESPERSON_MODULE_DECLARATIONS = [
    SalespersonHomeComponent,
    SalespersonNewComponent,
    SalespersonDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SalespersonRoutingModule { }