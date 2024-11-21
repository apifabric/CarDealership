import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Car-card.component.html',
  styleUrls: ['./Car-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Car-card]': 'true'
  }
})

export class CarCardComponent {


}