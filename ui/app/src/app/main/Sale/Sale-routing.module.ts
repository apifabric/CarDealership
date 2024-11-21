import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SaleHomeComponent } from './home/Sale-home.component';
import { SaleNewComponent } from './new/Sale-new.component';
import { SaleDetailComponent } from './detail/Sale-detail.component';

const routes: Routes = [
  {path: '', component: SaleHomeComponent},
  { path: 'new', component: SaleNewComponent },
  { path: ':id', component: SaleDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Sale-detail-permissions'
      }
    }
  }
];

export const SALE_MODULE_DECLARATIONS = [
    SaleHomeComponent,
    SaleNewComponent,
    SaleDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SaleRoutingModule { }