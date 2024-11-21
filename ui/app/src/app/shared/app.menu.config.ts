import { MenuRootItem } from 'ontimize-web-ngx';

import { AccessoryCardComponent } from './Accessory-card/Accessory-card.component';

import { CarCardComponent } from './Car-card/Car-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { RepairCardComponent } from './Repair-card/Repair-card.component';

import { SaleCardComponent } from './Sale-card/Sale-card.component';

import { SalespersonCardComponent } from './Salesperson-card/Salesperson-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { WarrantyCardComponent } from './Warranty-card/Warranty-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Accessory', name: 'ACCESSORY', icon: 'view_list', route: '/main/Accessory' }
    
        ,{ id: 'Car', name: 'CAR', icon: 'view_list', route: '/main/Car' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Repair', name: 'REPAIR', icon: 'view_list', route: '/main/Repair' }
    
        ,{ id: 'Sale', name: 'SALE', icon: 'view_list', route: '/main/Sale' }
    
        ,{ id: 'Salesperson', name: 'SALESPERSON', icon: 'view_list', route: '/main/Salesperson' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Warranty', name: 'WARRANTY', icon: 'view_list', route: '/main/Warranty' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AccessoryCardComponent

    ,CarCardComponent

    ,CustomerCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,RepairCardComponent

    ,SaleCardComponent

    ,SalespersonCardComponent

    ,ServiceCardComponent

    ,WarrantyCardComponent

];