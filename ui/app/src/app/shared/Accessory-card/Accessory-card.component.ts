import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Accessory-card.component.html',
  styleUrls: ['./Accessory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Accessory-card]': 'true'
  }
})

export class AccessoryCardComponent {


}