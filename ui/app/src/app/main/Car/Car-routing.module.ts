import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarHomeComponent } from './home/Car-home.component';
import { CarNewComponent } from './new/Car-new.component';
import { CarDetailComponent } from './detail/Car-detail.component';

const routes: Routes = [
  {path: '', component: CarHomeComponent},
  { path: 'new', component: CarNewComponent },
  { path: ':id', component: CarDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Car-detail-permissions'
      }
    }
  },{
    path: ':car_id/Inventory', loadChildren: () => import('../Inventory/Inventory.module').then(m => m.InventoryModule),
    data: {
        oPermission: {
            permissionId: 'Inventory-detail-permissions'
        }
    }
},{
    path: ':car_id/Sale', loadChildren: () => import('../Sale/Sale.module').then(m => m.SaleModule),
    data: {
        oPermission: {
            permissionId: 'Sale-detail-permissions'
        }
    }
},{
    path: ':car_id/Service', loadChildren: () => import('../Service/Service.module').then(m => m.ServiceModule),
    data: {
        oPermission: {
            permissionId: 'Service-detail-permissions'
        }
    }
},{
    path: ':car_id/Warranty', loadChildren: () => import('../Warranty/Warranty.module').then(m => m.WarrantyModule),
    data: {
        oPermission: {
            permissionId: 'Warranty-detail-permissions'
        }
    }
}
];

export const CAR_MODULE_DECLARATIONS = [
    CarHomeComponent,
    CarNewComponent,
    CarDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CarRoutingModule { }